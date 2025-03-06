![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShowExceptionDialog Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic612.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IWebHostExceptionListener Interface](topic607.md) : ShowExceptionDialog Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_path_
    The file path to an existing exception report which should be submitted.

Glossary Item Box

Displays an ExceptionReportDialog in the host application. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub ShowExceptionDialog( _
       ByVal _path_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IWebHostExceptionListener](topic607.md)
    Dim path As String
     
    instance.ShowExceptionDialog(path)  
  
C#|   
---|---  
      
    
    void ShowExceptionDialog( 
       string _path_
    )  
  
#### Parameters

 _path_
    The file path to an existing exception report which should be submitted.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IWebHostExceptionListener Interface](topic607.md)   
[IWebHostExceptionListener Members](topic608.md)

©2024 DriveWorks Ltd. All Rights Reserved.
