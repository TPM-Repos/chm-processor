Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConsistencyLevelChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacro Class](topic11429.md) : ConsistencyLevelChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [ConsistencyLevel](topic11444.md) property is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ConsistencyLevelChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacro](topic11429.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.ConsistencyLevelChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> ConsistencyLevelChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacro Class](topic11429.md)   
[SpecificationMacro Members](topic11430.md)


