RelativeToDirectory Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : RelativeToDirectory Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Specifies how relative paths are handled. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum RelativeToDirectory 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RelativeToDirectory](topic2359.md)  
  
C#|   
---|---  
      
    
    public enum RelativeToDirectory : System.Enum   
  
# Members

Member| Description  
---|---  
**Auto**|  For a project, this is equivalent to [Project](topic2359.md), for a specification it is equivalent to [Specification](topic2359.md).  
**GroupContent**|  Relative paths are resolved relative to the groups' content directory if it is set, otherwise null is returned.  
**Project**|  Relative paths are resolved relative to the project directory, for a specification, this means the original project directory.  
**Specification**|  Relative paths are resolved relative to the specification directory. For a project, this is equivalent to [Project](topic2359.md).  
**SpecificationMetadata**|  Relative paths are resolved relative to the specification metadata directory. For a project, this is equivalent to [Project](topic2359.md).  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.RelativeToDirectory**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks Namespace](topic2159.md)


