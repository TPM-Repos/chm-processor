       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UseLocalValueFormat Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [DriveControlValueTask Class](topic12245.md) : UseLocalValueFormat Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether the control value should be converted using the rules for the current culture before driving it into the control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property UseLocalValueFormat As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DriveControlValueTask](topic12245.md)
    Dim value As Boolean
     
    instance.UseLocalValueFormat = value
     
    value = instance.UseLocalValueFormat  
  
C#|   
---|---  
      
    
    public bool UseLocalValueFormat {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveControlValueTask Class](topic12245.md)   
[DriveControlValueTask Members](topic12246.md)


