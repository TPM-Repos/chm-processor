Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CopiedSpecificationFile Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : CopiedSpecificationFile Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised after a specification file has successfully been copied to the target location. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event CopiedSpecificationFile As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.CopiedSpecificationFile, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> CopiedSpecificationFile  
  
# Remarks

This event will get raised for every file that has been copied as a part of the specification.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


