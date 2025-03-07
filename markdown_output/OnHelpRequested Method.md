Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnHelpRequested Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : OnHelpRequested Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_hevent_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Sub OnHelpRequested( _
       ByVal _hevent_ As HelpEventArgs _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim hevent As HelpEventArgs
     
    instance.OnHelpRequested(hevent)  
  
C#|   
---|---  
      
    
    protected override void OnHelpRequested( 
       HelpEventArgs _hevent_
    )  
  
#### Parameters

 _hevent_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)


