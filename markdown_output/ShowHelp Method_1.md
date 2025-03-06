ShowHelp Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ICaptureViewHost Interface](topic13363.md) : ShowHelp Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_topicName_
    The name of the help topic to show.

Glossary Item Box

Shows the help for the given topic name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub ShowHelp( _
       ByVal _topicName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICaptureViewHost](topic13363.md)
    Dim topicName As String
     
    instance.ShowHelp(topicName)  
  
C#|   
---|---  
      
    
    void ShowHelp( 
       string _topicName_
    )  
  
#### Parameters

 _topicName_
    The name of the help topic to show.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICaptureViewHost Interface](topic13363.md)   
[ICaptureViewHost Members](topic13364.md)


