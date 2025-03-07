Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectDetails Class   
[Members](topic4331.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ProjectDetails Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides information about a registered DriveWorks project. 

# Object Model

![](dotnetdiagramimages/image205.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="{Name}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    <SerializableAttribute()>
    Public NotInheritable Class ProjectDetails   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDetails](topic4330.md)  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="{Name}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    [SerializableAttribute()]
    public sealed class ProjectDetails   
  
# Remarks

Modifications made to an instance of ProjectDetails are not immediately reflected in the group from which the instance was obtained. To apply any modifications, call the [GroupProjects.TryUpdateProject](topic3236.md) method.

# Inheritance Hierarchy

System.Object  
**DriveWorks.ProjectDetails**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDetails Members](topic4331.md)   
[DriveWorks Namespace](topic2159.md)


