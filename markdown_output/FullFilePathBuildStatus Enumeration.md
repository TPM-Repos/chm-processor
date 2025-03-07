Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FullFilePathBuildStatus Enumeration   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : FullFilePathBuildStatus Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the different states of building a full file path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum FullFilePathBuildStatus 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FullFilePathBuildStatus](topic13451.md)  
  
C#|   
---|---  
      
    
    public enum FullFilePathBuildStatus : System.Enum   
  
# Members

Member| Description  
---|---  
**Failed**|  Full file path could not be built.  
**PreventedOverwrite**|  Built full file path points to an existing file.  
**Success**|  Full file path was successfully built.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.SolidWorks.FullFilePathBuildStatus**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.SolidWorks Namespace](topic13345.md)


