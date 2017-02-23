import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main {
    
    public static final String SEPARATOR = "@";
    /*
     * Complete the function below.
     *
 	 * Note: The questions in this test build upon each other. We recommend you
	 * copy your solutions to your text editor of choice before proceeding to
	 * the next question as you will not be able to revisit previous questions.
	 */
 

    static int countHoldings(String input) {
        String splitArr[] = input.split("@");
        return splitArr.length;
    }

    public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        int res;
        String _input;
        try {
            _input = in.nextLine();
        } catch (Exception e) {
            _input = null;
        }
        res = countHoldings(_input);
        System.out.println(res);
    }
}

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Arrays;


public class Main {
    
    public static final String SEPARATOR = "@";
    public static final String COLON = ":";
    
    /*
     * Complete the function below.
     *
	 * Note: The questions in this test build upon each other. We recommend you
	 * copy your solutions to your text editor of choice before proceeding to
	 * the next question as you will not be able to revisit previous questions.
	 */

    static void printHoldings(String portfolioString) {
        int i;
        String strArray[] = portfolioString.split("@") ;
        int len = strArray.length;
        Arrays.sort(strArray);
        
        for (i =0; i<len;i++){
            strArray[i] = strArray[i].replace(",",", ");
        }
        for (i =0; i<len-1;i++){
            System.out.print("["+strArray[i]+"], ");
        }
        System.out.print("["+strArray[i]+"]");
    }
    
    
    public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        String res;
        String _input;
        try {
            _input = in.nextLine();
        } catch (Exception e) {
            _input = null;
        }
        printHoldings(_input);
    }
}



import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Arrays;


public class Main {
    
    public static final String SEPARATOR = "@";
    public static final String COLON = ":";
    
    /*
     * Complete the function below.
     *
	 * Note: The questions in this test build upon each other. We recommend you
	 * copy your solutions to your text editor of choice before proceeding to
	 * the next question as you will not be able to revisit previous questions.
	 */

    static void printHoldings(String portfolioString) {
        int i;
        String strArray[] = portfolioString.split(":") ;
        String newArr = strArray[1];
        strArray = newArr.split("@") ;
        int len = strArray.length;
        Arrays.sort(strArray);
        
        for (i =0; i<len;i++){
            strArray[i] = strArray[i].replace(",",", ");
        }
        for (i =0; i<len-1;i++){
            System.out.print("["+strArray[i]+"], ");
        }
        System.out.print("["+strArray[i]+"]");
    }
    
    
    public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        String res;
        String _input;
        try {
            _input = in.nextLine();
        } catch (Exception e) {
            _input = null;
        }
        printHoldings(_input);
    }
}




import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Arrays;


public class Main {
    
    public static final String SEPARATOR = "@";
    public static final String COLON = ":";
    static void printHoldings(String portfolioString) {
        int i;
        String strArray[] = portfolioString.split(":") ;
        String portfolio = strArray[0];
        String benchmark = strArray[1];
        String portArray[] = portfolio.split("@");
        String benchArray[] = benchmark.split("@");
        int len = portArray.length;
        Arrays.sort(portArray);
        Arrays.sort(benchArray);
        
        String resArray[] = new String[len];
        
        for (i =0; i<len;i++){
            String temp1[] = portArray[i].split(",");
            String temp2[] = benchArray[i].split(",");
            String r = "";
            if(Integer.parseInt(temp1[2]) > Integer.parseInt(temp2[2])) {
                int diff = Integer.parseInt(temp1[2]) - Integer.parseInt(temp2[2]);
                r = "SELL, "+temp1[0]+", "+Integer.toString(diff)+".00";
            } else {
                int diff = Integer.parseInt(temp2[2]) - Integer.parseInt(temp1[2]);
                r = "BUY, "+temp1[0]+", "+Integer.toString(diff)+".00";
            }
            resArray[i] = r;
        }

        for (i =0; i<len-1;i++){
            System.out.print("["+resArray[i]+"], ");
        }
            System.out.print("["+resArray[i]+"]");

    }
    
    
    public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        String res;
        String _input;
        try {
            _input = in.nextLine();
        } catch (Exception e) {
            _input = null;
        }
        printHoldings(_input);
    }
}




import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Arrays;


public class Main {
    
    public static final String SEPARATOR = "@";
    public static final String COLON = ":";
    static void printHoldings(String portfolioString) {
        int i;
        String strArray[] = portfolioString.split(":") ;
        String portfolio = strArray[0];
        String benchmark = strArray[1];
        String portArray[] = portfolio.split("@");
        String benchArray[] = benchmark.split("@");
        int len = portArray.length;
        Arrays.sort(portArray);
        Arrays.sort(benchArray);
        DecimalFormat df = new DecimalFormat("0.00");
        df.setMaximumFractionDigits(2);
        String resArray[] = new String[len];
        float portfolioValue = 0;
        for (i =0; i<len;i++){
            String temp1[] = portArray[i].split(",");
            String temp2[] = benchArray[i].split(",");
            portfolioValue += Float.parseFloat(temp1[2]) * Float.parseFloat(temp2[3]);
        }

        for (i =0; i<len;i++){
            String temp1[] = portArray[i].split(",");
            String temp2[] = benchArray[i].split(",");
            float val = Float.parseFloat(temp1[2]) * Float.parseFloat(temp2[3]);
            float nav = val*100/portfolioValue;
            String nval = df.format(val);
            String nnav = df.format(nav);
            String temp = df.format(Float.parseFloat(temp2[3]));
            String r = temp1[0]+", "+temp1[1]+", "+temp1[2]+", "+temp+", "+nval+", "+nnav;
            resArray[i] = r;
        }

        for (i =0; i<len-1;i++){
            System.out.print("["+resArray[i]+"], ");
        }
            System.out.print("["+resArray[i]+"]");

    }
    
    
    public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        String res;
        String _input;
        try {
            _input = in.nextLine();
        } catch (Exception e) {
            _input = null;
        }
        printHoldings(_input);
    }
}






import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Arrays;


public class Main {
    
    public static final String SEPARATOR = "@";
    public static final String COLON = ":";
    static void printHoldings(String portfolioString) {
        int i;
        String strArray[] = portfolioString.split(":") ;
        String portfolio = strArray[0];
        String benchmark = strArray[1];
        String portArray[] = portfolio.split("@");
        String benchArray[] = benchmark.split("@");
        int len = portArray.length;
        Arrays.sort(portArray);
        Arrays.sort(benchArray);
        DecimalFormat df = new DecimalFormat("0.00");
        df.setMaximumFractionDigits(2);
        String resArray[] = new String[len];
        float portfolioValue = 0;
        float benchValue = 0;
        for (i =0; i<len;i++){
            String temp1[] = portArray[i].split(",");
            String temp2[] = benchArray[i].split(",");
            portfolioValue += Float.parseFloat(temp1[2]) * Float.parseFloat(temp2[3]);
            benchValue += Float.parseFloat(temp2[2]) * Float.parseFloat(temp2[3]);
        }
        float diff;
        if (portfolioValue > benchValue){
            diff = portfolioValue - benchValue;
        } else {
            diff = benchValue - portfolioValue;
        }
        
        for (i =0; i<len;i++){
            String temp1[] = portArray[i].split(",");
            String temp2[] = benchArray[i].split(",");
            float val = Float.parseFloat(temp2[2]) * Float.parseFloat(temp2[3]);
            float nav = val*100/benchValue;
            float amt = nav * diff/100;
            String trans = "";
            float valDiff;
            float resVal;
            if (Float.parseFloat(temp1[2]) * Float.parseFloat(temp2[3]) > Float.parseFloat(temp2[2]) * Float.parseFloat(temp2[3])) {
                valDiff = Float.parseFloat(temp1[2]) * Float.parseFloat(temp2[3]) - Float.parseFloat(temp2[2]) * Float.parseFloat(temp2[3]);
                trans = "SELL";
                resVal = (amt + valDiff)/Float.parseFloat(temp2[3]);
            } else {
                valDiff = Float.parseFloat(temp2[2]) * Float.parseFloat(temp2[3]) - Float.parseFloat(temp1[2]) * Float.parseFloat(temp2[3]);
                trans = "BUY";
                resVal = (amt - valDiff)/Float.parseFloat(temp2[3]);
            }
            
            String nval = df.format(val);
            String nnav = df.format(nav);
            float temp = Math.abs(Float.parseFloat(df.format(resVal)));
            if (trans == "SELL"){
              temp = 0 - temp;  
            }
            String nresVal = df.format(temp);
            String r = trans + ", " + temp1[0]+ ", "+nresVal;
            resArray[i] = r;
        }

        for (i =0; i<len-1;i++){
            System.out.print("["+resArray[i]+"], ");
        }
            System.out.print("["+resArray[i]+"]");

    }
    
    
    public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        String res;
        String _input;
        try {
            _input = in.nextLine();
        } catch (Exception e) {
            _input = null;
        }
        printHoldings(_input);
    }
}




