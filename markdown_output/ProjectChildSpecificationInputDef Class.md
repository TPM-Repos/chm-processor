Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectChildSpecificationInputDef Class   
[Members](topic4048.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ProjectChildSpecificationInputDef Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides access to an input mapping for a given project in a child specification definition. 

# Object Model

![](dotnetdiagramimages/image188.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public NotInheritable Class ProjectChildSpecificationInputDef 
       Inherits DomainObject
       Implements [DriveWorks.Abstractions.IHasRule](topic5947.md), [DriveWorks.Abstractions.IHasRuleId](topic5957.md), [DriveWorks.Abstractions.IHasRuleVersionHistory](topic5975.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationInputDef](topic4047.md)  
  
C#|   
---|---  
      
    
    public sealed class ProjectChildSpecificationInputDef : DomainObject, [DriveWorks.Abstractions.IHasRule](topic5947.md), [DriveWorks.Abstractions.IHasRuleId](topic5957.md), [DriveWorks.Abstractions.IHasRuleVersionHistory](topic5975.md)    
  
# Remarks

When a child specification is created by the specifier, DriveWorks drives values from the parent specification into constants in the child specification. Each value to be driven into a constant is described by an instance of the [ProjectChildSpecificationInputDef](topic4047.md) type.

# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
**DriveWorks.ProjectChildSpecificationInputDef**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationInputDef Members](topic4048.md)   
[DriveWorks Namespace](topic2159.md)


