/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package deletebackspace;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 *
 * @author Ham

Interview question from Samsung (from HackerRank)

Given an array of chars (of keys pressed), remove r"\b" and the preceding char.
Notes:
    1.  This is NOT the single backspace char ('\b'), but 2 consecutive
        chars: a backslash char ('\') followed by a 'b'
    2.  Must handle multiple occurrences of "\b", might be adjacent.
    3.  Must handle (possibly multiple) "\b" at the beginning of the array.
    4.  Must handle _excessive_ "\b"; i.e. more "\b" than avail chars.
    5.  No special treatment for other backslash-combo;
        i.e. treat them normally as 2 consecutive chars.
        e.g. "\1\b2" => "\2" (deleting "1")
             "\\bA"  => "A"  (deleting the first '\')

Input:
    1 line representing the keypress array
    (might contain leading and trailing spaces)

Output:
    The original input line
    Then the resulting line after processing r"\b"
 */
public class DeleteBackspace {

    private static final Pattern p_lead_bs = Pattern.compile("^(\\\\b)+");
    private static final Pattern p_non_lead_bs = Pattern.compile(".\\\\b");

    public static String delete_backspace(String s) {
        System.out.println("orig=<" + s + ">");

        boolean found;
        Matcher m;
    
        do {
            //m = p_lead_bs.matcher(s);
            //s = m.replaceFirst("");

            m = p_non_lead_bs.matcher(s);
            found = m.find();
            s = m.replaceFirst("");
            //System.out.println("loop=<" + s + ">");
        } while (found);

        System.out.println("last=<" + s + ">");
        return s;
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        delete_backspace("\\1\\b2: '1' removed");
        delete_backspace("\\\\bA: first '\\' removed");
        delete_backspace("123\\b\\bABC: '23' removed bc consecutive bs");
        delete_backspace("\\b\\b\\b  with lead\\bDing bs A\\bB and em\\bMbedde\\bEd some\\b\\b\\bOMEwhere");
        delete_backspace("\\b\\b\\b\\b123456\\b\\b\\b\\b\\b\\b\\b\\b\\b\\bExtra bs removed");
    }
}
