Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IApplicationPlugin Interface   
[Members](topic2005.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) : IApplicationPlugin Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a contract for a plugin to a DriveWorks application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Interface IApplicationPlugin 
       Inherits [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationPlugin](topic2004.md)  
  
C#|   
---|---  
      
    
    public interface IApplicationPlugin : [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Remarks

A class which implements this interface must also be marked with the [ApplicationPluginAttribute](topic2106.md) attribute to be recognized as an application plugin.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationPlugin Members](topic2005.md)   
[DriveWorks.Applications.Extensibility Namespace](topic1995.md)


