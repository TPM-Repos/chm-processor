Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnCheckedFileExists Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) : OnCheckedFileExists Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The event sender.

_filePath_
    The file path to include with the event.

Glossary Item Box

Raises the [CheckedFileExists](topic1679.md) event with the provided file path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub OnCheckedFileExists( _
       ByVal _sender_ As Object, _
       ByVal _filePath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim sender As Object
    Dim filePath As String
     
    instance.OnCheckedFileExists(sender, filePath)  
  
C#|   
---|---  
      
    
    void OnCheckedFileExists( 
       object _sender_ ,
       string _filePath_
    )  
  
#### Parameters

 _sender_
    The event sender.
_filePath_
    The file path to include with the event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)


