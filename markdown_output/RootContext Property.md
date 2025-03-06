RootContext Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : RootContext Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the root [SpecificationContext](topic11149.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property RootContext As [SpecificationContext](topic11149.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As [SpecificationContext](topic11149.md)
     
    value = instance.RootContext  
  
C#|   
---|---  
      
    
    public [SpecificationContext](topic11149.md) RootContext {get;}  
  
# Remarks

If this is already a root level context, it will return itself.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


