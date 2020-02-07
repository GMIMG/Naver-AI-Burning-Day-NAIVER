package com.muticampus.ex01;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;



import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


//Object Detection API ����
public class APIExamFace {

 public static void main(String[] args) {
	 
	 
	 
     //String jsonText =  "{\"isMarried\":false,\"address\":null,\"name\":\"kim\",\"age\":19}";
     JSONParser parser = new JSONParser();
     JSONObject obj = null;

	 
	 
	 
	 

     StringBuffer reqStr = new StringBuffer();
     String clientId = "cbxhzui4en";//���ø����̼� Ŭ���̾�Ʈ ���̵�";
     String clientSecret = "m7YcN6l15L4l4hSgVRTfAiArIHbEK8S384Q55fIX";//���ø����̼� Ŭ���̾�Ʈ ��ũ����";
     String str;

     try {
         String paramName = "image"; // �Ķ���͸��� image�� ����
         String imgFile = "22.jpg";
         File uploadFile = new File(imgFile);
         String apiURL = "https://naveropenapi.apigw.ntruss.com/vision-obj/v1/detect"; // ��ü �ν�
         URL url = new URL(apiURL);
         HttpURLConnection con = (HttpURLConnection)url.openConnection();
         con.setUseCaches(false);
         con.setDoOutput(true);
         con.setDoInput(true);
         // multipart request
         String boundary = "---" + System.currentTimeMillis() + "---";
         con.setRequestProperty("Content-Type", "multipart/form-data; boundary=" + boundary);
         con.setRequestProperty("X-NCP-APIGW-API-KEY-ID", clientId);
         con.setRequestProperty("X-NCP-APIGW-API-KEY", clientSecret);
         OutputStream outputStream = con.getOutputStream();
         PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
         String LINE_FEED = "\r\n";
         // file �߰�
         String fileName = uploadFile.getName();
         writer.append("--" + boundary).append(LINE_FEED);
         writer.append("Content-Disposition: form-data; name=\"" + paramName + "\"; filename=\"" + fileName + "\"").append(LINE_FEED);
         writer.append("Content-Type: "  + URLConnection.guessContentTypeFromName(fileName)).append(LINE_FEED);
         writer.append(LINE_FEED);
         writer.flush();
         FileInputStream inputStream = new FileInputStream(uploadFile);
         byte[] buffer = new byte[4096];
         int bytesRead = -1;
         while ((bytesRead = inputStream.read(buffer)) != -1) {
             outputStream.write(buffer, 0, bytesRead);
         }
         outputStream.flush();
         inputStream.close();
         writer.append(LINE_FEED).flush();
         writer.append("--" + boundary + "--").append(LINE_FEED);
         writer.close();
         BufferedReader br = null;
         int responseCode = con.getResponseCode();
         if(responseCode==200) { // ���� ȣ��
             br = new BufferedReader(new InputStreamReader(con.getInputStream()));
         } else {  // ���� �߻�
             System.out.println("error!!!!!!! responseCode= " + responseCode);
             br = new BufferedReader(new InputStreamReader(con.getInputStream()));
         }
         String inputLine;
         if(br != null) {
             StringBuffer response = new StringBuffer();
             while ((inputLine = br.readLine()) != null) {
                 response.append(inputLine);
             }
             br.close();
             
             
             
             
             
             
             str = response.toString();
             System.out.println(str);
             
             
             
             
             
           //Object 
             //JSONArray array = (JSONArray) jsonObject.get("address"); for(int i=0; i<array.size(); i++){ JSONObject result = (JSONObject) array.get(i); System.out.println("result :: " +result.get("zipcode")); }


             


             
             try {
                 obj = (JSONObject)parser.parse(str);
            } catch (ParseException e) {
                 System.out.println("��ȯ�� ����");
                 e.printStackTrace();
            }
            
             
             JSONObject jsonObject = (JSONObject) obj;
             
             System.out.println(obj.get("predictions"));
             JSONArray array = (JSONArray) jsonObject.get("predictions");
             
             JSONObject result = (JSONObject) array.get(0);
             System.out.println("result :: " +result.get("detection_boxes"));


             
             //obj = (JSONObject)parser.parse(obj.get("predictions").toString());
             //obj = (JSONObject)parser.parse(obj.get(0).toString());
             
            System.out.println(obj);
             
             
         } else {
             System.out.println("error !!!");
         }
     } catch (Exception e) {
         System.out.println(e);
     }
 }
}


