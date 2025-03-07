Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ApplicationPluginInfo Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ApplicationPluginLoadedEventArgs Class](topic2116.md) : ApplicationPluginInfo Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets information about the application plugin that was loaded. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ApplicationPluginInfo As [IApplicationPluginInfo](topic2010.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ApplicationPluginLoadedEventArgs](topic2116.md)
    Dim value As [IApplicationPluginInfo](topic2010.md)
     
    value = instance.ApplicationPluginInfo  
  
C#|   
---|---  
      
    
    public [IApplicationPluginInfo](topic2010.md) ApplicationPluginInfo {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ApplicationPluginLoadedEventArgs Class](topic2116.md)   
[ApplicationPluginLoadedEventArgs Members](topic2117.md)


