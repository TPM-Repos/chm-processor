Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ActiveDialogOrForm Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : ActiveDialogOrForm Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the active dialog if one is shown, otherwise, gets the active form. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ActiveDialogOrForm As [SpecificationForm](topic11402.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As [SpecificationForm](topic11402.md)
     
    value = instance.ActiveDialogOrForm  
  
C#|   
---|---  
      
    
    public [SpecificationForm](topic11402.md) ActiveDialogOrForm {get;}  
  
# Remarks

If a specification isn't running, a null reference (Nothing in Visual Basic) is returned.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


