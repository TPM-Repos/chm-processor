SpecificationId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) : SpecificationId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the identifier of the specification to which the release results belong. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property SpecificationId As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentsResults](topic6300.md)
    Dim value As Integer
     
    value = instance.SpecificationId  
  
C#|   
---|---  
      
    
    public int SpecificationId {get;}  
  
# Remarks

This will be the root specification if we are an embedded child specification.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)


