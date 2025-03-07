Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DocumentGenerationOptions Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : DocumentGenerationOptions Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides possible values for the document generation setting which governs when documents get generated using the default specification-flow. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <FlagsAttribute()>
    Public Enum DocumentGenerationOptions 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DocumentGenerationOptions](topic10768.md)  
  
C#|   
---|---  
      
    
    [FlagsAttribute()]
    public enum DocumentGenerationOptions : System.Enum   
  
# Members

Member| Description  
---|---  
**Both**|  Documents always get generated.  
**Finish**|  Documents get generated on finish.  
**Release**|  Documents get generated on release.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Specification.DocumentGenerationOptions**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Specification Namespace](topic10764.md)


