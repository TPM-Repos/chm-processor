TemporaryDesignMasterPath Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : TemporaryDesignMasterPath Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the fully-qualified path to the context's temporary copy of the design-master. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property TemporaryDesignMasterPath As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As String
     
    value = instance.TemporaryDesignMasterPath  
  
C#|   
---|---  
      
    
    public string TemporaryDesignMasterPath {get;}  
  
#### Property Value

The fully-qualified path to the context's temporary copy of the design-master if the context is in a running state, otherwise, a null reference (Nothing in Visual Basic).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


