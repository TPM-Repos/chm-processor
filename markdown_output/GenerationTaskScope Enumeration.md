Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerationTaskScope Enumeration   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : GenerationTaskScope Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Specifies the type of SOLIDWORKS components a [GenerationTask](topic13678.md) support. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <FlagsAttribute()>
    Public Enum GenerationTaskScope 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationTaskScope](topic13452.md)  
  
C#|   
---|---  
      
    
    [FlagsAttribute()]
    public enum GenerationTaskScope : System.Enum   
  
# Members

Member| Description  
---|---  
**All**|  Specifies that the [GenerationTask](topic13678.md) supports running on all types of components.  
**Assemblies**|  Specifies that the [GenerationTask](topic13678.md) supports running on assemblies.  
**Drawings**|  Specifies that the [GenerationTask](topic13678.md) supports running on drawings.  
**Parts**|  Specifies that the [GenerationTask](topic13678.md) supports running on parts.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.SolidWorks.GenerationTaskScope**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.SolidWorks Namespace](topic13345.md)


