       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationPropertiesResult Enumeration   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2363.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : SpecificationPropertiesResult Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the result of trying to retrieve the properties for a Specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum SpecificationPropertiesResult 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationPropertiesResult](topic2363.md)  
  
C#|   
---|---  
      
    
    public enum SpecificationPropertiesResult : System.Enum   
  
# Members

Member| Description  
---|---  
**AccessDenied**|  The specification properties file could not be accessed. This could be due to insufficient permissions.  
**FileMissing**|  The specification properties could not be loaded because the specification file could not be found.  
**InvalidXml**|  The specification properties could not be loaded because the XML was malformed.  
**Success**|  The specification properties were loaded successfully.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.SpecificationPropertiesResult**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.
