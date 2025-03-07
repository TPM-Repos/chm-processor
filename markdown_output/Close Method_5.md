Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Close Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IGroupConnectorEditor Interface](topic1716.md) : Close Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_save_
    Whether or not to save changes in current editor back into the connector.

Glossary Item Box

Called by the connector management view to notify the connector view UI that it is being closed by the user. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function Close( _
       ByVal _save_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupConnectorEditor](topic1716.md)
    Dim save As Boolean
    Dim value As Boolean
     
    value = instance.Close(save)  
  
C#|   
---|---  
      
    
    bool Close( 
       bool _save_
    )  
  
#### Parameters

 _save_
    Whether or not to save changes in current editor back into the connector.

#### Return Value

False to abort closing the view, otherwise true. Please note that no message will be shown to the user if the close is aborted, therefore it is up to the view to let the user know why the close was aborted.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupConnectorEditor Interface](topic1716.md)   
[IGroupConnectorEditor Members](topic1717.md)


