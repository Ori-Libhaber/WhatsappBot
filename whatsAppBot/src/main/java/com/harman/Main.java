package com.harman;


import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import javax.swing.JOptionPane;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeDriverService;
import static org.openqa.selenium.chrome.ChromeDriverService.CHROME_DRIVER_EXE_PROPERTY;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Ori
 */
public class Main {

    public static void main(String[] args) throws InterruptedException {

        System.getProperties().setProperty(CHROME_DRIVER_EXE_PROPERTY, "D:\\selenium\\webDriver\\chromedriver.exe");

        WebDriver wd = new ChromeDriver(ChromeDriverService.createDefaultService());
        wd.manage().window().setSize(new Dimension(1024, 768));
        Thread.sleep(7000);
        wd.get("https://web.whatsapp.com/");

        JOptionPane.showMessageDialog(null, "Please login to whatsAppwWeb");
        Executors.newScheduledThreadPool(1).scheduleAtFixedRate(() -> {
            try {
                wd.findElement(By.xpath("//*[@title='KOKO']")).click();
                try {
                    TimeUnit.SECONDS.sleep(1);
                } catch (InterruptedException ex) {
                    // do nothing
                }
                List<WebElement> messges = wd.findElements(By.xpath("//span[@class='emojitext selectable-text']"));
                messges.forEach((WebElement message) -> {
                    if ("bbb".equals(message.getText())) {
                        JOptionPane.showMessageDialog(null, "I got your message master!");
                    }
                    System.out.println(message.getText());
                });
            } catch (NoSuchElementException ex) {
                // do nothing
            }
        }, 0, 5, TimeUnit.SECONDS);

    }

}
