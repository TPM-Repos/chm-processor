Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FilePathsDisplayValue Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedTriggeredAction Class](topic5123.md) : FilePathsDisplayValue Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the pipe delimited string of the file paths that the triggered action is waiting for. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property FilePathsDisplayValue As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedTriggeredAction](topic5123.md)
    Dim value As String
     
    instance.FilePathsDisplayValue = value
     
    value = instance.FilePathsDisplayValue  
  
C#|   
---|---  
      
    
    public string FilePathsDisplayValue {get; set;}  
  
# Remarks

This is to be used when displaying the calculated file paths in the UI.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedTriggeredAction Class](topic5123.md)   
[ReleasedTriggeredAction Members](topic5124.md)


