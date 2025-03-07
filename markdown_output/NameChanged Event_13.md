Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NameChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SpecificationMacroCategory Class](topic5359.md) : NameChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the name of the project category changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event NameChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacroCategory](topic5359.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.NameChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> NameChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacroCategory Class](topic5359.md)   
[SpecificationMacroCategory Members](topic5360.md)


