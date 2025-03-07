Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnInformationSet Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [GroupConnectorBase<T> Class](topic1857.md) : OnInformationSet Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    The information to set.

Glossary Item Box

Sets the connector's information. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub OnInformationSet( _
       ByVal _info_ As T _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectorBase(Of T)](topic1857.md)
    Dim info As T
     
    instance.OnInformationSet(info)  
  
C#|   
---|---  
      
    
    protected virtual void OnInformationSet( 
       T _info_
    )  
  
#### Parameters

 _info_
    The information to set.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupConnectorBase<T> Class](topic1857.md)   
[GroupConnectorBase<T> Members](topic1858.md)


