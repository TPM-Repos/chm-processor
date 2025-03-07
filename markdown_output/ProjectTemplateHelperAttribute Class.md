Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectTemplateHelperAttribute Class   
[Members](topic2145.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) : ProjectTemplateHelperAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Supports automatic discovery of project template helpers in a library. 

# Object Model

![](dotnetdiagramimages/image76.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=True, 
       Inherited=True)>
    Public Class ProjectTemplateHelperAttribute 
       Inherits [DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTemplateHelperAttribute](topic2144.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=true, 
       Inherited=true)]
    public class ProjectTemplateHelperAttribute : [DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)   
  
# Remarks

DriveWorks applications use this attribute to discover the project template helpers exposed by a library.

# Inheritance Hierarchy

System.Object  
System.Attribute  
[DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)  
**DriveWorks.Applications.Extensibility.ProjectTemplateHelperAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTemplateHelperAttribute Members](topic2145.md)   
[DriveWorks.Applications.Extensibility Namespace](topic1995.md)


