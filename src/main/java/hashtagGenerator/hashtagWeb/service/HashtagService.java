package hashtagGenerator.hashtagWeb.service;

import org.springframework.stereotype.Service;
import org.springframework.util.ObjectUtils;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;

@Service
public class HashtagService {

    public String fileHandler(MultipartFile multipartFile) throws Exception {

        //시간 형태로 파일 저장
       SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyyMMdd");
        String current_date = simpleDateFormat.format(new Date());

        //절대경로 저
        String absolutePath = new File("").getAbsolutePath() + "/";

        String path = "images/" + current_date;
        File file = new File(path);

        if(!file.exists())
            file.mkdirs();

        if(!multipartFile.isEmpty()) {
            //jpeg,png.gif 파일만 처리
            String contentType = multipartFile.getContentType();
            String originalFileExtension;
            if (ObjectUtils.isEmpty(contentType))
                return "fail";
            else {
                if (contentType.contains("image/jpeg"))
                    originalFileExtension = ".jpg";
                else if (contentType.contains(("image/png")))
                    originalFileExtension = ".png";
                else if (contentType.contains("image/gif"))
                    originalFileExtension = ".gif";
                else
                    return "fail";
            }

            String newFileName = Long.toString(System.nanoTime()) + originalFileExtension;
            String savedFileName = absolutePath + path + "/" + newFileName;
            file = new File(absolutePath + path + "/" + newFileName);
            multipartFile.transferTo(file);
            return savedFileName;
        }
        else
            return "fail";

    }

}
