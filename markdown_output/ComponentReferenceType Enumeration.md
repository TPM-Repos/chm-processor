Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentReferenceType Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) : ComponentReferenceType Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Specifies whether a component is a standard or a derived component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum ComponentReferenceType 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentReferenceType](topic6144.md)  
  
C#|   
---|---  
      
    
    public enum ComponentReferenceType : System.Enum   
  
# Members

Member| Description  
---|---  
**Derived**|  The component is derived from another component and when released has a reference action of [ReleasedComponentReferenceAction.Derive](topic6146.md).  
**Standard**|  The component is a standard child component and when released has a reference action of [ReleasedComponentReferenceAction.Replace](topic6146.md).  
  
# Remarks

Derived components with blank component names inherits their name from their parent component.

Derived components do not register their component names in the group.

# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Components.ComponentReferenceType**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Components Namespace](topic6089.md)


