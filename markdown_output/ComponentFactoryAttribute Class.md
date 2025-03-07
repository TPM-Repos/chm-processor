Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentFactoryAttribute Class   
[Members](topic6168.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) : ComponentFactoryAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Used to indicate to DriveWorks the factory that is responsible for creating components of a given type. 

# Object Model

![](dotnetdiagramimages/image317.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=False, 
       Inherited=True)>
    Public Class ComponentFactoryAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentFactoryAttribute](topic6167.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=false, 
       Inherited=true)]
    public class ComponentFactoryAttribute : System.Attribute   
  
# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Components.ComponentFactoryAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentFactoryAttribute Members](topic6168.md)   
[DriveWorks.Components Namespace](topic6089.md)


