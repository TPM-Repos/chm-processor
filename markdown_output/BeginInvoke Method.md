Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginInvoke Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ISafeProjectExecutor Interface](topic2303.md) : BeginInvoke Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_action_
    

Glossary Item Box

Invokes an action asynchronously on the same thread as the dispatcher. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub BeginInvoke( _
       ByVal _action_ As Action _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISafeProjectExecutor](topic2303.md)
    Dim action As Action
     
    instance.BeginInvoke(action)  
  
C#|   
---|---  
      
    
    void BeginInvoke( 
       Action _action_
    )  
  
#### Parameters

 _action_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISafeProjectExecutor Interface](topic2303.md)   
[ISafeProjectExecutor Members](topic2304.md)


