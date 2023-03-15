#include "a2.h"

int bitwise_xor(int value){
    //return result of performing a bit-wise XOR operation on <value>
    //returns integer value

    int res[7];
    int val = 0; 
    int ascii = KEY; //get ASCII int of KEY character

    int code[7] = {64, 32, 16, 8, 4, 2, 1};
    int binary[7]; 
    int k_binary[7]; 
    //int *binary;

    //printf("KEY: %d\n", ascii);
    
    //get binary of char c
    for (int i = 0; i<7; i++){
        if (value-code[i] >=0){
            binary[i] = 1;
            value = value-code[i];
        } else{
            binary[i] = 0;
        }

        //printf("Binary: %d %d\n", i, binary[i]);

        //get binary of ascii
        if (ascii-code[i] >=0){
            k_binary[i] = 1;
            ascii = ascii-code[i];
        } else{
            k_binary[i] = 0;
        }

        //printf("K_Binary: %d %d\n", i, k_binary[i]);

    }

   for (int i = 0; i<7; i++){
        if (binary[i] == 0 && k_binary[i] == 0){
            //strcat(res, "0");
          res[i] = 0;
        } else if (binary[i] == 1 && k_binary[i] == 1){
            //strcat(res, "0");
          res[i] = 0;
        } else{
            //strcat(res, "1");
          res[i] = 1;
        }
      //printf("res: %d\n", res[i]);
      
    }

    if (res[0] == 1){
      val = val + 64;
    }
    if (res[1] == 1){
      val = val + 32;
    }
    if (res[2] == 1){
      val = val + 16;
    }
    if (res[3] == 1){
      val = val + 8;
    }
    if (res[4] == 1){
      val = val + 4;
    }
    if (res[5] == 1){
      val = val + 2;
    }
    if (res[6] == 1){
      val = val + 1;
    }

  return val;
}



char *xor_encrypt(char c){
    //return pointer to 7-digit string of '1's and '0's

    char *res;
    res = (char *)calloc(8, sizeof(char)); //!!!!
    int val = c; //get ASCII int of char c
    int ascii = KEY; //get ASCII int of KEY character

    int code[7] = {64, 32, 16, 8, 4, 2, 1};
    int binary[7]; 
    int k_binary[7]; 
    //int *binary;


    //get binary of char c
    for (int i = 0; i<7; i++){
        if (val-code[i] >=0){
            binary[i] = 1;
            //strcat(res, "1");
            val = val-code[i];
        } else{
            //strcat(res, "0");
            binary[i] = 0;
        }

        //get binary of ascii
        if (ascii-code[i] >=0){
            k_binary[i] = 1;
            //strcat(res, "1");
            ascii = ascii-code[i];
        } else{
            //strcat(res, "0");
            k_binary[i] = 0;
        }

    }

    
    for (int i = 0; i<7; i++){
        if (binary[i] == 0 && k_binary[i] == 0){
            //strcat(res, "0");
            res[i] = '0';
        } else if (binary[i] == 1 && k_binary[i] == 1){
            //strcat(res, "0");
            res[i] = '0';
        } else{
            //strcat(res, "1");
            res[i] = '1';
        }

    }

    //printf("%s\n", res);
    return res;
}

char xor_decrypt(char *s){
    //return character obtained after evaluating ASCII value

    int code[7] = {64, 32, 16, 8, 4, 2, 1};
    int val = 0;
    char c_res;
    int res;

    int ascii = KEY; //convert KEY to ascii int
    int binary[7];
    int k_binary[7];
    int r_binary[7];
    
    
    for (int i = 0; i<7; i++){
        //binary[i] = (int)s[i]; //put s into int array

        //printf("%d", binary[i]);
        //get binary of ascii
        if (ascii-code[i] >=0){
            k_binary[i] = 1;
            ascii = ascii-code[i];
        } else{
            k_binary[i] = 0;
        }

    }


    for (int i = 0; i<7; i++){
        if (s[i] == '0' && k_binary[i] == 0){
            r_binary[i] = 0;
        } else if (s[i] == '1' && k_binary[i] == 1){
            r_binary[i] = 0;
        } else{
            r_binary[i] = 1;
        }

    }

    for (int i = 0; i<7; i++){

        //printf("%d\n", r_binary[i]);
        if (r_binary[i] == 1){
            val = val + code[i];
        } 
        

    }
    
    //printf("%d", val);
    
    //res = abs(ascii-val);
    
    c_res = val;

    return c_res;


}

char *gen_code(char *msg){
    //return pointer to a 256-digit string of '1's and '0's


    
    //printf("%s\n", msg);
  
    //convert each char to binary
    int len = strlen(msg);
    //char *temp;
  
    char* binary_arr;
    binary_arr = (char *)calloc((len*7)+7, sizeof(char));
    int count = 0;
    int count_ba = 0;
    char* encrypted;
    encrypted = (char *)calloc(8, sizeof(char));
    int track = 5;
    int t = 5;
    int calc = 0;

    //allocate memory for 256 digit code
    char *code;
    code = (char *)malloc(257*sizeof(char));

    for (int i = 0; i<256; i++){
      code[i] = '0';
    }

    code[256] = '\0';


    //get binary of every character in msg and put in array
    while (count <= len){

        char *temp = xor_encrypt(msg[count]);
     
        //strcpy(encrypted,xor_encrypt(msg[count])); //!!!!
        strcpy(encrypted, temp);

        for (int i = 0; i<7; i++){
            binary_arr[count_ba] = encrypted[i];
            count_ba++; //keeps track of how many elements are in binary arr
        }
        //printf("binary num %s\n", binary_arr);
        free(temp);
        count ++;
        
    }
  


    
        
    while (calc<count_ba){

      //printf("hi");

      if (binary_arr[calc] == '1'){
        code[t] = '1';
        //printf("C: %d T: %d\n", calc, t);
        //track++;
    } 

      if (t == 10 || t == 26 || t == 42 || t == 58){
        t = t+11;
      } else if (t == 74){
        t = t+6;
      }else if (t == 175 || t == 191 || t == 207 || t == 223 || t == 239){
        t = t+6;
      } else{
        t++;
      }
      //printf("T: %d\n", t);
      calc++;

      
    }

    //printf("count_ba: %d\n", count_ba);
    //printf("binary num %s\n", binary_arr);

    for (int i = 0; i<5; i++){
        code[i] = '1';
    }

  for (int i = 11; i<17; i++){
        code[i] = '1';
    }


    code[20] = '1';
    code[27] = '1';
    code[31] = '1';
    

    code[32] = '1';
    code[33] = '0'; 
    code[34] = '1'; 
    code[35] = '0'; 
    code[36] = '1';



    code[43] = '1';
    code[44] = '0'; 
    code[45] = '1'; 
    code[46] = '0'; 
    code[47] = '1';
  
    code[48] = '1';
    code[49] = '0'; 
    code[50] = '0'; 
    code[51] = '0'; 
    code[52] = '1'; 



    code[59] = '1';
    code[60] = '0'; 
    code[61] = '0'; 
    code[62] = '0'; 
    code[63] = '1';

    code[64] = '1';
    code[65] = '1'; 
    code[66] = '1'; 
    code[67] = '1'; 
    code[68] = '1';


    code[75] = '1';
    code[76] = '1'; 
    code[77] = '1'; 
    code[78] = '1'; 
    code[79] = '1';

  code[176] = '1';
  code[177] = '1'; 
  code[178] = '1'; 
  code[179] = '1'; 
  code[180] = '1';

  code[192] = '1';
  code[193] = '0'; 
  code[194] = '0'; 
  code[195] = '0'; 
  code[196] = '1';

  code[208] = '1';
  code[209] = '0'; 
  code[210] = '1'; 
  code[211] = '0'; 
  code[212] = '1';

  code[224] = '1';
  code[225] = '0'; 
  code[226] = '0'; 
  code[227] = '0'; 
  code[228] = '1';
  
  code[240] = '1';
  code[241] = '1'; 
  code[242] = '1'; 
  code[243] = '1'; 
  code[244] = '1';

  code[255] = '1';
  

  //printf("%s\n", code);

  free(binary_arr);
  free(encrypted);
  //free(code);
  

  return code;
}

char *read_code(char *code){
    //add code here

    //printf("CODE: %s\n", code);
    char *binary_arr;
    char *res = (char *)calloc(26, sizeof(char));
    char *temp_code = (char *)calloc(7, sizeof(char));
    char letter;
    binary_arr = (char *)calloc(26*8, sizeof(char));
    int track = 5;
    int count = 0;
    int num = 0;

  //printf("Hi\n");
    //from 256 long char string, get the values that were encrypted
    for (int i = 0; i<180;i++){ 
      binary_arr[i] = code[track];

      if (track == 10 || track == 26 || track == 42 || track == 58){
        track = track + 11;
      } else if (track == 74){
        track = track + 6;
      }else if (track == 175 || track == 191 || track == 207 || track == 223 || track == 239){
        track = track + 6;
      } else{
        track++;
      }

      
      //printf("%d\n", i);
      //printf("%c", binary_arr[i]);
    }

    while (count < 26){
      
      for (int j = 0; j<7; j++){
        temp_code[j] = binary_arr[num]; //get 7-digit binary code
        letter = xor_decrypt(temp_code); //convert it to a char
        num++;
      }

      res[count] = letter; //add decrypted letter to res
      count++;
      
    }
    
    free(temp_code);
    free(binary_arr);

    return res;

}

//SNEHA 
char *compress(char *code){
  char *res= malloc(sizeof(char)*65); 
  char *compare = malloc(sizeof(char)*5);  
  char* ptr = code; 
  
  for (int counter = 0; counter<64;counter++){
    strncpy(compare, ptr, 4); 
    compare[4] = '\0'; 
    if (strcmp(compare, "0000")==0){
      res[counter]= '0';
    }
    if (strcmp(compare, "0001")==0){
      res[counter]= '1';
    }
    if (strcmp(compare, "0010")==0){
      res[counter]= '2';
    }
    if (strcmp(compare, "0011")==0){
      res[counter]= '3';
    }
    if (strcmp(compare, "0100")==0){
      res[counter]= '4';
    }
    if (strcmp(compare, "0101")==0){
      res[counter]= '5';
    }
    if (strcmp(compare, "0110")==0){
      res[counter]= '6';
    }
    if (strcmp(compare, "0111")==0){
      res[counter]= '7';
    }
    if (strcmp(compare, "1000")==0){
      res[counter]= '8';
    }
    if (strcmp(compare, "1001")==0){
      res[counter]= '9';
    }
    if (strcmp(compare, "1010")==0){
      res[counter]= 'A';
    }
    if (strcmp(compare, "1011")==0){
      res[counter]= 'B';
    }
    if (strcmp(compare, "1100")==0){
      res[counter]= 'C';
    }
    if (strcmp(compare, "1101")==0){
      res[counter]= 'D';
    }
    if (strcmp(compare, "1110")==0){
      res[counter]= 'E';
    }
    if (strcmp(compare, "1111")==0){
      res[counter]= 'F';
    } 
    ptr ++ ;
    ptr ++ ;
    ptr ++ ;
    ptr ++ ; 
  } 
  free(compare);
  res[64] ='\0'; 
  return (res); 
}

char *decompress(char *code){
  char *res= malloc(sizeof(char)*257); 
  char *compare = malloc(sizeof(char)*2);  
  char* ptr = code; 
  
  for (int counter = 0; counter<256;counter=counter+4){
    strncpy(compare, ptr, 1); 
    compare[1] = '\0'; 
    if (strcmp(compare, "0")==0){
      res[counter]= '0';
      res[counter+1]= '0';
      res[counter+2]= '0';
      res[counter+3]= '0';
      
    }
    if (strcmp(compare, "1")==0){
      res[counter]= '0';
      res[counter+1]= '0';
      res[counter+2]= '0';
      res[counter+3]= '1';
    }
    if (strcmp(compare, "2")==0){
      res[counter]= '0';
      res[counter+1]= '0';
      res[counter+2]= '1';
      res[counter+3]= '0';
    }
    if (strcmp(compare, "3")==0){
      res[counter]= '0';
      res[counter+1]= '0';
      res[counter+2]= '1';
      res[counter+3]= '1';
    }
    if (strcmp(compare, "4")==0){
      res[counter]= '0';
      res[counter+1]= '1';
      res[counter+2]= '0';
      res[counter+3]= '0';
    }
    if (strcmp(compare, "5")==0){
      res[counter]= '0';
      res[counter+1]= '1';
      res[counter+2]= '0';
      res[counter+3]= '1';
    }
    if (strcmp(compare, "6")==0){
      res[counter]= '0';
      res[counter+1]= '1';
      res[counter+2]= '1';
      res[counter+3]= '0';
    }
    if (strcmp(compare, "7")==0){
      res[counter]= '0';
      res[counter+1]= '1';
      res[counter+2]= '1';
      res[counter+3]= '1';
    }
    if (strcmp(compare, "8")==0){
      res[counter]= '1';
      res[counter+1]= '0';
      res[counter+2]= '0';
      res[counter+3]= '0';
    }
    if (strcmp(compare, "9")==0){
      res[counter]= '1';
      res[counter+1]= '0';
      res[counter+2]= '0';
      res[counter+3]= '1';
    }
    if (strcmp(compare, "A")==0){
      res[counter]= '1';
      res[counter+1]= '0';
      res[counter+2]= '1';
      res[counter+3]= '0';
    }
    if (strcmp(compare, "B")==0){
      res[counter]= '1';
      res[counter+1]= '0';
      res[counter+2]= '1';
      res[counter+3]= '1';
    }
    if (strcmp(compare, "C")==0){
      res[counter]= '1';
      res[counter+1]= '1';
      res[counter+2]= '0';
      res[counter+3]= '0';
    }
    if (strcmp(compare, "D")==0){
      res[counter]= '1';
      res[counter+1]= '1';
      res[counter+2]= '0';
      res[counter+3]= '1';
    }
    if (strcmp(compare, "E")==0){
      res[counter]= '1';
      res[counter+1]= '1';
      res[counter+2]= '1';
      res[counter+3]= '0';
    }
    if (strcmp(compare, "F")==0){
      res[counter]= '1';
      res[counter+1]= '1';
      res[counter+2]= '1';
      res[counter+3]= '1';
    } 
    ptr ++ ; 
  } 
  free(compare);
  res[256] ='\0'; 
  return (res); 
}

int calc_ld(char *sandy, char *cima){
    //we better not have to worry ab runtime...
  int helper (char *sandy, char *cima, int s_len, int c_len);
  int s_len = strlen(sandy); 
  int c_len =strlen(cima);
  int result = 0; 
  result = helper (sandy, cima, s_len, c_len); 
  return result; 
}

int helper (char *sandy, char *cima, int s_len, int c_len){
  int sneha = 0;
  int balaji =0; 
  int hi = 0; 
  int result = 0; 
  
  //for empty strings: 
  if (c_len==0){
    return s_len;
  }
  
  if (s_len==0){
    return c_len;
  }
  
   
  if(sandy[s_len-1]==cima[c_len-1]){
    return helper(sandy, cima, s_len-1, c_len-1); 
  }
   
  hi = helper(sandy, cima, s_len-1, c_len); 
  sneha = helper(sandy, cima, s_len-1, c_len-1); 
  balaji = helper(sandy, cima, s_len, c_len-1);

  
  if (hi<sneha && hi<balaji){
    sneha = hi; 
  }
  else if (balaji<sneha && balaji<hi){
    sneha = balaji; 
  }
  else if (hi == balaji && hi<sneha) {
    sneha = hi; 
  }
  return sneha +1; 
}

