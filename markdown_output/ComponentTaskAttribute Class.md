Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTaskAttribute Class   
[Members](topic6456.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) : ComponentTaskAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Attribute to be assigned to implementors of the [IComponentTask](topic6393.md) interface to provide additional information about the task. 

# Object Model

![](dotnetdiagramimages/image335.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=False, 
       Inherited=True)>
    Public MustInherit Class ComponentTaskAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskAttribute](topic6455.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=false, 
       Inherited=true)]
    public abstract class ComponentTaskAttribute : System.Attribute   
  
# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Components.Tasks.ComponentTaskAttribute**  
[DriveWorks.SolidWorks.GenerationTaskAttribute](topic13693.md)  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskAttribute Members](topic6456.md)   
[DriveWorks.Components.Tasks Namespace](topic6391.md)


