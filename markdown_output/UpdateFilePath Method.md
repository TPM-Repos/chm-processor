       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpdateFilePath Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5134.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedTriggeredAction Class](topic5123.md) : UpdateFilePath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_pathToChange_
    An existing file path that the triggered action is looking for.

_newPath_
    The new path to replace the old location with.

Glossary Item Box

Updates the specified file path to the new location. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub UpdateFilePath( _
       ByVal _pathToChange_ As String, _
       ByVal _newPath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedTriggeredAction](topic5123.md)
    Dim pathToChange As String
    Dim newPath As String
     
    instance.UpdateFilePath(pathToChange, newPath)  
  
C#|   
---|---  
      
    
    public void UpdateFilePath( 
       string _pathToChange_ ,
       string _newPath_
    )  
  
#### Parameters

 _pathToChange_
    An existing file path that the triggered action is looking for.
_newPath_
    The new path to replace the old location with.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedTriggeredAction Class](topic5123.md)   
[ReleasedTriggeredAction Members](topic5124.md)

©2024 DriveWorks Ltd. All Rights Reserved.
