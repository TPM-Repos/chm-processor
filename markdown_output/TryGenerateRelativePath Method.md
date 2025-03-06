       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGenerateRelativePath Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13592.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) : TryGenerateRelativePath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_originalPath_
    The source path for an additional file.

_newPath_
    The resulting new path for the additional file.

Glossary Item Box

Helper method for using the "Relative Path" parameter value to create a new path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Function TryGenerateRelativePath( _
       ByVal _originalPath_ As String, _
       ByRef _newPath_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerator](topic13579.md)
    Dim originalPath As String
    Dim newPath As String
    Dim value As Boolean
     
    value = instance.TryGenerateRelativePath(originalPath, newPath)  
  
C#|   
---|---  
      
    
    protected bool TryGenerateRelativePath( 
       string _originalPath_ ,
       ref string _newPath_
    )  
  
#### Parameters

 _originalPath_
    The source path for an additional file.
_newPath_
    The resulting new path for the additional file.

#### Return Value

Whether or not generation is possible based on the result of the new path.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)

©2024 DriveWorks Ltd. All Rights Reserved.
