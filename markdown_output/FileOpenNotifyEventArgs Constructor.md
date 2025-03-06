![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileOpenNotifyEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13659.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileOpenNotifyEventArgs Class](topic13653.md) : FileOpenNotifyEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_filename_
    The name of the file that was opened.

Glossary Item Box

Creates a new instance of the [FileOpenNotifyEventArgs](topic13653.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _filename_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim filename As String
     
    Dim instance As New [FileOpenNotifyEventArgs](topic13653.md)(filename)  
  
C#|   
---|---  
      
    
    public FileOpenNotifyEventArgs( 
       string _filename_
    )  
  
#### Parameters

 _filename_
    The name of the file that was opened.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileOpenNotifyEventArgs Class](topic13653.md)   
[FileOpenNotifyEventArgs Members](topic13654.md)

©2024 DriveWorks Ltd. All Rights Reserved.
