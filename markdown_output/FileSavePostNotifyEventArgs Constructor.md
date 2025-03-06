![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileSavePostNotifyEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13667.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileSavePostNotifyEventArgs Class](topic13661.md) : FileSavePostNotifyEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_saveType_
    Type of save as defined in swFileSaveTypes_e.

_filename_
    The name of the file that was saved.

Glossary Item Box

Creates a new instance of the [FileSavePostNotifyEventArgs](topic13661.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _saveType_ As Integer, _
       ByVal _filename_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim saveType As Integer
    Dim filename As String
     
    Dim instance As New [FileSavePostNotifyEventArgs](topic13661.md)(saveType, filename)  
  
C#|   
---|---  
      
    
    public FileSavePostNotifyEventArgs( 
       int _saveType_ ,
       string _filename_
    )  
  
#### Parameters

 _saveType_
    Type of save as defined in swFileSaveTypes_e.
_filename_
    The name of the file that was saved.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileSavePostNotifyEventArgs Class](topic13661.md)   
[FileSavePostNotifyEventArgs Members](topic13662.md)

©2024 DriveWorks Ltd. All Rights Reserved.
