       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationType Enumeration   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10772.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationType Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the type of a specification, i.e. whether it was newly created, copied, etc. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum SpecificationType 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationType](topic10772.md)  
  
C#|   
---|---  
      
    
    public enum SpecificationType : System.Enum   
  
# Members

Member| Description  
---|---  
**Copied**|  The specification is a copy of an existing specification.  
**Existing**|  The specification is an opened existing specification.  
**New**|  The specification is a new specification.  
**NotLoaded**|  The specification hasn't been loaded.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Specification.SpecificationType**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Specification Namespace](topic10764.md)

©2024 DriveWorks Ltd. All Rights Reserved.
