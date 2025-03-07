Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnPreviousInvoking Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [WizardBase Class](topic1200.md) : OnPreviousInvoking Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_e_
    

Glossary Item Box

Raises the [PreviousInvoking](topic1256.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub OnPreviousInvoking( _
       ByVal _e_ As CancelEventArgs _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WizardBase](topic1200.md)
    Dim e As CancelEventArgs
     
    instance.OnPreviousInvoking(e)  
  
C#|   
---|---  
      
    
    protected virtual void OnPreviousInvoking( 
       CancelEventArgs _e_
    )  
  
#### Parameters

 _e_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WizardBase Class](topic1200.md)   
[WizardBase Members](topic1201.md)


