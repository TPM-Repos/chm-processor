![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileExistenceCheckEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1855.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [FileExistenceCheckEventArgs Class](topic1849.md) : FileExistenceCheckEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_filePath_
    The file path of the file that is having its existence checked.

Glossary Item Box

Creates a new [FileExistenceCheckEventArgs](topic1849.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _filePath_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim filePath As String
     
    Dim instance As New [FileExistenceCheckEventArgs](topic1849.md)(filePath)  
  
C#|   
---|---  
      
    
    public FileExistenceCheckEventArgs( 
       string _filePath_
    )  
  
#### Parameters

 _filePath_
    The file path of the file that is having its existence checked.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileExistenceCheckEventArgs Class](topic1849.md)   
[FileExistenceCheckEventArgs Members](topic1850.md)

©2024 DriveWorks Ltd. All Rights Reserved.
