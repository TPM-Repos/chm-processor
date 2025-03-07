Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Load(EngineHost,XElement) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) > [Load Method](topic6310.md) : Load(EngineHost,XElement) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_engineHost_
    The engine host.

_savedResults_
    The saved release results.

Glossary Item Box

Loads the released component results from the given XML. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Load( _
       ByVal _engineHost_ As EngineHost, _
       ByVal _savedResults_ As XElement _
    ) As [ReleaseComponentsResults](topic6300.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim engineHost As EngineHost
    Dim savedResults As XElement
    Dim value As [ReleaseComponentsResults](topic6300.md)
     
    value = [ReleaseComponentsResults](topic6300.md).Load(engineHost, savedResults)  
  
C#|   
---|---  
      
    
    public static [ReleaseComponentsResults](topic6300.md) Load( 
       EngineHost _engineHost_ ,
       XElement _savedResults_
    )  
  
#### Parameters

 _engineHost_
    The engine host.
_savedResults_
    The saved release results.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)   
[Overload List](topic6310.md)


