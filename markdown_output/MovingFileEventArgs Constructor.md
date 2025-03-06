![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MovingFileEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [MovingFileEventArgs Class](topic1888.md) : MovingFileEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourcePath_
    The file path of the file that is being moved.

_targetPath_
    The file path that the file is being moved to.

Glossary Item Box

Creates a new [MovingFileEventArgs](topic1888.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _sourcePath_ As String, _
       ByVal _targetPath_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim sourcePath As String
    Dim targetPath As String
     
    Dim instance As New [MovingFileEventArgs](topic1888.md)(sourcePath, targetPath)  
  
C#|   
---|---  
      
    
    public MovingFileEventArgs( 
       string _sourcePath_ ,
       string _targetPath_
    )  
  
#### Parameters

 _sourcePath_
    The file path of the file that is being moved.
_targetPath_
    The file path that the file is being moved to.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[MovingFileEventArgs Class](topic1888.md)   
[MovingFileEventArgs Members](topic1889.md)


