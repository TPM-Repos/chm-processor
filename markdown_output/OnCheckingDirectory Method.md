Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnCheckingDirectory Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) : OnCheckingDirectory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    

_directoryPath_
    

Glossary Item Box

Raises the [CheckingDirectory](topic1680.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub OnCheckingDirectory( _
       ByVal _sender_ As Object, _
       ByVal _directoryPath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim sender As Object
    Dim directoryPath As String
     
    instance.OnCheckingDirectory(sender, directoryPath)  
  
C#|   
---|---  
      
    
    void OnCheckingDirectory( 
       object _sender_ ,
       string _directoryPath_
    )  
  
#### Parameters

 _sender_
    
_directoryPath_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)


