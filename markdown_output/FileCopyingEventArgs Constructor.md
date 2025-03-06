![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileCopyingEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [FileCopyingEventArgs Class](topic2859.md) : FileCopyingEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourcePath_
    The fully-qualified path to the source file.

_targetPath_
    The fully-qualified destination path the file will be copied to.

Glossary Item Box

Creates a new instance of the [FileCopyingEventArgs](topic2859.md) class. 

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
     
    Dim instance As New [FileCopyingEventArgs](topic2859.md)(sourcePath, targetPath)  
  
C#|   
---|---  
      
    
    public FileCopyingEventArgs( 
       string _sourcePath_ ,
       string _targetPath_
    )  
  
#### Parameters

 _sourcePath_
    The fully-qualified path to the source file.
_targetPath_
    The fully-qualified destination path the file will be copied to.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileCopyingEventArgs Class](topic2859.md)   
[FileCopyingEventArgs Members](topic2860.md)


