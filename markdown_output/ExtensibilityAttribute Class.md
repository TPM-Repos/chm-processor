Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExtensibilityAttribute Class   
[Members](topic7178.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) : ExtensibilityAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a base class for all attributes applied to a extension library. 

# Object Model

![](dotnetdiagramimages/image386.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=False, 
       Inherited=True)>
    Public MustInherit Class ExtensibilityAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExtensibilityAttribute](topic7177.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=false, 
       Inherited=true)]
    public abstract class ExtensibilityAttribute : System.Attribute   
  
# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Extensibility.ExtensibilityAttribute**  
[DriveWorks.Applications.Extensibility.ProjectTemplateHelperAttribute](topic2144.md)  
[DriveWorks.Applications.SettingsPageAttribute](topic959.md)  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExtensibilityAttribute Members](topic7178.md)   
[DriveWorks.Extensibility Namespace](topic7150.md)


