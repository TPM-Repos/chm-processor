Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ApplicationPluginLoadedEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ApplicationPluginLoadedEventArgs Class](topic2116.md) : ApplicationPluginLoadedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_applicationPluginInfo_
    Information about the application plugin that was loaded.

Glossary Item Box

Initializes a new instance of the [ApplicationPluginLoadedEventArgs](topic2116.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _applicationPluginInfo_ As [IApplicationPluginInfo](topic2010.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim applicationPluginInfo As [IApplicationPluginInfo](topic2010.md)
     
    Dim instance As New [ApplicationPluginLoadedEventArgs](topic2116.md)(applicationPluginInfo)  
  
C#|   
---|---  
      
    
    public ApplicationPluginLoadedEventArgs( 
       [IApplicationPluginInfo](topic2010.md) _applicationPluginInfo_
    )  
  
#### Parameters

 _applicationPluginInfo_
    Information about the application plugin that was loaded.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ApplicationPluginLoadedEventArgs Class](topic2116.md)   
[ApplicationPluginLoadedEventArgs Members](topic2117.md)


