Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ApplicationPluginAttribute Class   
[Members](topic2107.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) : ApplicationPluginAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides information about an application plugin to a DriveWorks Application. 

# Object Model

![](dotnetdiagramimages/image72.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=False, 
       Inherited=False)>
    Public NotInheritable Class ApplicationPluginAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ApplicationPluginAttribute](topic2106.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=false, 
       Inherited=false)]
    public sealed class ApplicationPluginAttribute : System.Attribute   
  
# Remarks

A class which implements the [IApplicationPlugin](topic2004.md) interface must also be marked with this attribute to be recognized as an application plugin.

# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Applications.Extensibility.ApplicationPluginAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ApplicationPluginAttribute Members](topic2107.md)   
[DriveWorks.Applications.Extensibility Namespace](topic1995.md)


