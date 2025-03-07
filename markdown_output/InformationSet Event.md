Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InformationSet Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [GroupConnectorBase<T> Class](topic1857.md) : InformationSet Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the connector's information has been set. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event InformationSet As EventHandler(Of T)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectorBase(Of T)](topic1857.md)
    Dim handler As EventHandler(Of T)
     
    AddHandler instance.InformationSet, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<T> InformationSet  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupConnectorBase<T> Class](topic1857.md)   
[GroupConnectorBase<T> Members](topic1858.md)


