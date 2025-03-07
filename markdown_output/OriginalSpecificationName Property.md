Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OriginalSpecificationName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : OriginalSpecificationName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

If the specification is in a transition, gets the name of the specification passed to the [Open](topic11190.md) method when the specification was originally opened. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property OriginalSpecificationName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As String
     
    value = instance.OriginalSpecificationName  
  
C#|   
---|---  
      
    
    public string OriginalSpecificationName {get;}  
  
#### Property Value

The original name of the specification, see the remarks for details.

# Remarks

This property only returns a value during a transition for a specification opened by a call to the [Open](topic11190.md) method.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


