![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentReferenceType Enumeration   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6144.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) : ComponentReferenceType Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Specifies whether a component is a standard or a derived component. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum ComponentReferenceType 
       Inherits System.Enum  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentReferenceType](topic6144.md)  
  
C#|   
---|---  
      
    
    public enum ComponentReferenceType : System.Enum   
  
# ![](dotnetimages/collapse.gif)Members

Member| Description  
---|---  
**Derived**|  The component is derived from another component and when released has a reference action of [ReleasedComponentReferenceAction.Derive](topic6146.md).  
**Standard**|  The component is a standard child component and when released has a reference action of [ReleasedComponentReferenceAction.Replace](topic6146.md).  
  
# ![](dotnetimages/collapse.gif)Remarks

Derived components with blank component names inherits their name from their parent component.

Derived components do not register their component names in the group.

# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Components.ComponentReferenceType**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.Components Namespace](topic6089.md)

©2024 DriveWorks Ltd. All Rights Reserved.
