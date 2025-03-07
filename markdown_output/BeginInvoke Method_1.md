Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginInvoke Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [BasicLockSafeProjectExecutor Class](topic2430.md) : BeginInvoke Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_action_
    The action to run.

Glossary Item Box

Invokes an action asynchronously on a new thread. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub BeginInvoke( _
       ByVal _action_ As Action _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [BasicLockSafeProjectExecutor](topic2430.md)
    Dim action As Action
     
    instance.BeginInvoke(action)  
  
C#|   
---|---  
      
    
    public void BeginInvoke( 
       Action _action_
    )  
  
#### Parameters

 _action_
    The action to run.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[BasicLockSafeProjectExecutor Class](topic2430.md)   
[BasicLockSafeProjectExecutor Members](topic2431.md)


